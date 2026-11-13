/**
 * End-to-End Integration Test: Partial Success & Retry Resilience
 * Author: Samir (Database + Prompts + QA Owner — Member 4)
 * Scope: Partial artifact failure -> Job marked 'partial' -> POST /retry -> Only missing artifact regenerated -> Job marked 'done'
 * Contract: docs/api-contracts.md (Section 2.6)
 */

const request = require('supertest');

const BASE_URL = process.env.API_URL || 'http://localhost:5000';
const SESSION_ID = 'test-e2e-partial-session-' + Date.now();

describe('E2E Partial Success & Retry Test Suite', () => {
  let partialJobId = 'c2d3e4f5-a6b7-8c9d-0e1f-2a3b4c5d6e7f'; // Seed partial job or uploaded job

  test('GET /api/jobs/:job_id should identify partial state with missing mindmap', async () => {
    const res = await request(BASE_URL)
      .get(`/api/jobs/${partialJobId}`)
      .expect(200);

    expect(res.body.id).toBe(partialJobId);
    expect(res.body.status).toBe('partial');
    expect(res.body.completed_artifacts).toEqual(
      expect.arrayContaining(['notes', 'cheatsheet'])
    );
    expect(res.body.completed_artifacts).not.toContain('mindmap');
    expect(res.body.error_message).toBeDefined();
  });

  test('Existing artifacts (notes, cheatsheet) should be accessible in partial state', async () => {
    // 1. Notes should succeed
    const notesRes = await request(BASE_URL)
      .get(`/api/jobs/${partialJobId}/outputs/notes`)
      .expect(200);
    expect(notesRes.body.type).toBe('notes');
    expect(notesRes.body.content.key_points.length).toBeGreaterThan(0);

    // 2. Cheatsheet should succeed
    const cheatsheetRes = await request(BASE_URL)
      .get(`/api/jobs/${partialJobId}/outputs/cheatsheet`)
      .expect(200);
    expect(cheatsheetRes.body.type).toBe('cheatsheet');
    expect(cheatsheetRes.body.content.sections.length).toBeGreaterThan(0);

    // 3. Mindmap should return 404 Not Found before retry
    await request(BASE_URL)
      .get(`/api/jobs/${partialJobId}/outputs/mindmap`)
      .expect(404);
  });

  test('POST /api/jobs/:job_id/retry should trigger generation ONLY for missing mindmap', async () => {
    const retryRes = await request(BASE_URL)
      .post(`/api/jobs/${partialJobId}/retry`)
      .expect(200);

    expect(retryRes.body.job_id).toBe(partialJobId);
    expect(['queued', 'processing', 'done']).toContain(retryRes.body.status);
    expect(retryRes.body.retried_artifacts).toContain('mindmap');
    expect(retryRes.body.retried_artifacts).not.toContain('notes');
    expect(retryRes.body.retried_artifacts).not.toContain('cheatsheet');

    // Poll until retry completes
    let status = retryRes.body.status;
    let attempts = 0;
    while (attempts < 20 && status !== 'done') {
      const pollRes = await request(BASE_URL).get(`/api/jobs/${partialJobId}`);
      status = pollRes.body.status;
      if (status === 'done') break;
      await new Promise((r) => setTimeout(r, 1000));
      attempts++;
    }

    expect(status).toBe('done');
  }, 25000);

  test('After retry, all 3 artifacts including mindmap should be fully available', async () => {
    const res = await request(BASE_URL)
      .get(`/api/jobs/${partialJobId}`)
      .expect(200);

    expect(res.body.status).toBe('done');
    expect(res.body.completed_artifacts).toEqual(
      expect.arrayContaining(['notes', 'cheatsheet', 'mindmap'])
    );

    // Verify mindmap is now accessible
    const mindmapRes = await request(BASE_URL)
      .get(`/api/jobs/${partialJobId}/outputs/mindmap`)
      .expect(200);
    expect(mindmapRes.body.type).toBe('mindmap');
    expect(mindmapRes.body.content).toHaveProperty('title');
    expect(mindmapRes.body.content).toHaveProperty('children');
  });
});
