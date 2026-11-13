/**
 * End-to-End Integration Test: Pipeline Happy Path
 * Author: Samir (Database + Prompts + QA Owner — Member 4)
 * Scope: Audio Upload -> Job Queued -> Polling -> Transcript -> Outputs (Notes, Cheatsheet, Mindmap) -> Done
 * Contract: docs/api-contracts.md
 */

const request = require('supertest');
const path = require('path');
const fs = require('fs');

const BASE_URL = process.env.API_URL || 'http://localhost:5000';
const SESSION_ID = 'test-e2e-happy-session-' + Date.now();

describe('E2E Pipeline Happy Path Test Suite', () => {
  let jobId;
  let recordingId;

  // 1. Upload Audio and Create Job
  test('POST /api/recordings/upload should accept audio and return 201 with queued job', async () => {
    // Create temporary audio buffer if sample audio file not present
    const dummyAudio = Buffer.from('RIFF....WAVEfmt ....data....');

    const res = await request(BASE_URL)
      .post('/api/recordings/upload')
      .set('x-session-id', SESSION_ID)
      .attach('file', dummyAudio, 'lecture_os_test.wav')
      .expect(201);

    expect(res.body).toHaveProperty('recording_id');
    expect(res.body).toHaveProperty('job_id');
    expect(res.body.status).toBe('queued');
    expect(res.body.filename).toBe('lecture_os_test.wav');

    recordingId = res.body.recording_id;
    jobId = res.body.job_id;
  });

  // 2. Poll Job Status until Done
  test('GET /api/jobs/:job_id should transition from queued/processing to done', async () => {
    expect(jobId).toBeDefined();

    let attempts = 0;
    const maxAttempts = 30; // 30 seconds max poll
    let status = 'queued';

    while (attempts < maxAttempts && status !== 'done' && status !== 'failed') {
      const res = await request(BASE_URL)
        .get(`/api/jobs/${jobId}`)
        .expect(200);

      expect(res.body.id).toBe(jobId);
      expect(res.body.recording_id).toBe(recordingId);
      status = res.body.status;

      expect(['queued', 'processing', 'done']).toContain(status);

      if (status === 'done') {
        expect(res.body.completed_artifacts).toEqual(
          expect.arrayContaining(['notes', 'cheatsheet', 'mindmap'])
        );
        expect(res.body.error_message).toBeNull();
        break;
      }

      await new Promise((r) => setTimeout(r, 1000));
      attempts++;
    }

    expect(status).toBe('done');
  }, 35000);

  // 3. Verify Transcript Structure
  test('GET /api/jobs/:job_id/transcript should return full transcript with timestamped segments', async () => {
    const res = await request(BASE_URL)
      .get(`/api/jobs/${jobId}/transcript`)
      .expect(200);

    expect(res.body).toHaveProperty('id');
    expect(res.body).toHaveProperty('full_text');
    expect(typeof res.body.full_text).toBe('string');
    expect(res.body.full_text.length).toBeGreaterThan(20);

    expect(Array.isArray(res.body.segments)).toBe(true);
    expect(res.body.segments.length).toBeGreaterThan(0);
    expect(res.body.segments[0]).toHaveProperty('start');
    expect(res.body.segments[0]).toHaveProperty('end');
    expect(res.body.segments[0]).toHaveProperty('text');

    expect(typeof res.body.word_count).toBe('number');
    expect(res.body.word_count).toBeGreaterThan(0);
  });

  // 4. Verify Generated Artifact: Notes
  test('GET /api/jobs/:job_id/outputs/notes should return structured notes conforming to schema', async () => {
    const res = await request(BASE_URL)
      .get(`/api/jobs/${jobId}/outputs/notes`)
      .expect(200);

    expect(res.body.type).toBe('notes');
    const content = res.body.content;

    expect(Array.isArray(content.key_points)).toBe(true);
    expect(content.key_points.length).toBeGreaterThan(0);

    expect(Array.isArray(content.definitions)).toBe(true);
    expect(content.definitions[0]).toHaveProperty('term');
    expect(content.definitions[0]).toHaveProperty('definition');

    expect(Array.isArray(content.examples)).toBe(true);
    expect(Array.isArray(content.quick_revision_sheet)).toBe(true);
  });

  // 5. Verify Generated Artifact: Cheatsheet
  test('GET /api/jobs/:job_id/outputs/cheatsheet should return high-yield sections with bullets', async () => {
    const res = await request(BASE_URL)
      .get(`/api/jobs/${jobId}/outputs/cheatsheet`)
      .expect(200);

    expect(res.body.type).toBe('cheatsheet');
    const content = res.body.content;

    expect(Array.isArray(content.sections)).toBe(true);
    expect(content.sections.length).toBeGreaterThanOrEqual(1);

    const firstSection = content.sections[0];
    expect(firstSection).toHaveProperty('heading');
    expect(typeof firstSection.heading).toBe('string');
    expect(Array.isArray(firstSection.bullets)).toBe(true);
    expect(firstSection.bullets.length).toBeGreaterThanOrEqual(1);
  });

  // 6. Verify Generated Artifact: Mindmap
  test('GET /api/jobs/:job_id/outputs/mindmap should return recursive hierarchical taxonomy tree', async () => {
    const res = await request(BASE_URL)
      .get(`/api/jobs/${jobId}/outputs/mindmap`)
      .expect(200);

    expect(res.body.type).toBe('mindmap');
    const content = res.body.content;

    expect(content).toHaveProperty('title');
    expect(typeof content.title).toBe('string');
    expect(Array.isArray(content.children)).toBe(true);
    expect(content.children.length).toBeGreaterThan(0);

    // Verify first child node schema
    const firstChild = content.children[0];
    expect(firstChild).toHaveProperty('title');
    expect(Array.isArray(firstChild.children)).toBe(true);
  });
});
