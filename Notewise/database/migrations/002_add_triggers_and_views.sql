-- 002_add_triggers_and_views.sql
-- Notewise Database Triggers & Analytical Views
-- Managed by Member 4 (Samir - Database + Prompts + QA Owner)

-- 1. Function to update updated_at timestamp on row modification
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 2. Trigger on jobs table to maintain accurate updated_at
DROP TRIGGER IF EXISTS trigger_update_jobs_timestamp ON jobs;
CREATE TRIGGER trigger_update_jobs_timestamp
    BEFORE UPDATE ON jobs
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- 3. Pipeline Summary View for Admin and Monitoring Dashboard
-- Aggregates job status, transcript word count, and generated artifacts in a single query
CREATE OR REPLACE VIEW v_job_pipeline_summary AS
SELECT 
    j.id AS job_id,
    j.status AS job_status,
    j.error_message,
    j.created_at AS job_created_at,
    j.updated_at AS job_updated_at,
    r.id AS recording_id,
    r.session_id,
    r.original_filename,
    t.word_count,
    COALESCE(
        jsonb_agg(
            jsonb_build_object(
                'type', o.type,
                'created_at', o.created_at
            )
        ) FILTER (WHERE o.id IS NOT NULL), 
        '[]'::jsonb
    ) AS completed_outputs,
    COUNT(o.id) AS completed_outputs_count
FROM jobs j
JOIN recordings r ON j.recording_id = r.id
LEFT JOIN transcripts t ON t.job_id = j.id
LEFT JOIN outputs o ON o.job_id = j.id
GROUP BY j.id, r.id, t.id;

-- 4. Full-Text Search Index on Lecture Transcripts for Fast Grounded Search
CREATE INDEX IF NOT EXISTS idx_transcripts_fulltext 
ON transcripts USING gin(to_tsvector('english', full_text));
