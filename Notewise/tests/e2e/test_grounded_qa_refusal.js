/**
 * End-to-End Integration Test: Grounded Q&A & Refusal Guardrails
 * Author: Samir (Database + Prompts + QA Owner — Member 4)
 * Scope: Context-grounded Q&A against lecture transcript; strict refusal of out-of-scope queries
 * Contract: docs/api-contracts.md (Section 2.5)
 */

const request = require('supertest');

const BASE_URL = process.env.API_URL || 'http://localhost:5000';
const JOB_ID = 'b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e'; // Done job with OS Paging lecture

describe('E2E Grounded Q&A & Refusal Test Suite', () => {

  // 1. In-Scope Questions (Should return grounded: true)
  describe('In-Scope Grounded Queries', () => {
    test('POST /api/jobs/:job_id/qa should answer paging vs frame differences accurately', async () => {
      const res = await request(BASE_URL)
        .post(`/api/jobs/${JOB_ID}/qa`)
        .send({
          question: 'What is the difference between a page and a frame?'
        })
        .expect(200);

      expect(res.body).toHaveProperty('question');
      expect(res.body).toHaveProperty('answer');
      expect(res.body.grounded).toBe(true);

      const ans = res.body.answer.toLowerCase();
      expect(ans).toMatch(/logical/);
      expect(ans).toMatch(/physical/);
    });

    test('POST /api/jobs/:job_id/qa should answer page fault handling steps with transcript evidence', async () => {
      const res = await request(BASE_URL)
        .post(`/api/jobs/${JOB_ID}/qa`)
        .send({
          question: 'What happens when a page fault occurs?'
        })
        .expect(200);

      expect(res.body.grounded).toBe(true);
      const ans = res.body.answer.toLowerCase();
      expect(ans).toMatch(/trap/);
      expect(ans).toMatch(/backing store|disk/);
    });
  });

  // 2. Out-of-Scope Queries (Must return grounded: false and exact refusal contract)
  describe('Out-of-Scope Anti-Hallucination Refusals', () => {
    test('POST /api/jobs/:job_id/qa should strictly refuse sports trivia', async () => {
      const res = await request(BASE_URL)
        .post(`/api/jobs/${JOB_ID}/qa`)
        .send({
          question: 'Who won the 2024 ICC T20 Cricket World Cup?'
        })
        .expect(200);

      expect(res.body.grounded).toBe(false);
      expect(res.body.answer).toBe('This topic was not covered in the lecture.');
    });

    test('POST /api/jobs/:job_id/qa should strictly refuse unrelated programming languages or algorithms', async () => {
      const res = await request(BASE_URL)
        .post(`/api/jobs/${JOB_ID}/qa`)
        .send({
          question: 'How do you write a bubble sort in C++?'
        })
        .expect(200);

      expect(res.body.grounded).toBe(false);
      expect(res.body.answer).toBe('This topic was not covered in the lecture.');
    });

    test('POST /api/jobs/:job_id/qa should refuse general world knowledge', async () => {
      const res = await request(BASE_URL)
        .post(`/api/jobs/${JOB_ID}/qa`)
        .send({
          question: 'What is the distance between the Earth and the Sun?'
        })
        .expect(200);

      expect(res.body.grounded).toBe(false);
      expect(res.body.answer).toBe('This topic was not covered in the lecture.');
    });
  });

  // 3. Input Validation Edge Cases
  describe('Input Validation & Error Handling', () => {
    test('POST /api/jobs/:job_id/qa should return 400 when question is empty', async () => {
      const res = await request(BASE_URL)
        .post(`/api/jobs/${JOB_ID}/qa`)
        .send({ question: '   ' })
        .expect(400);

      expect(res.body).toHaveProperty('error');
    });

    test('POST /api/jobs/:job_id/qa should return 400 when question field is missing', async () => {
      const res = await request(BASE_URL)
        .post(`/api/jobs/${JOB_ID}/qa`)
        .send({})
        .expect(400);

      expect(res.body).toHaveProperty('error');
    });
  });
});
