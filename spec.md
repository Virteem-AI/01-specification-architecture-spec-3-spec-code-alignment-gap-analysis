# TaskFlow API - Specification

## Overview

The API manages tasks in memory using Flask.

## Endpoints

| Method | Path | Expected status | Description |
|---|---|---|---|
| POST | `/tasks` | 201 | Create a task |
| GET | `/tasks` | 200 | List tasks |
| GET | `/tasks/{id}` | 200 or 404 | Get a task |
| PUT | `/tasks/{id}` | 200 or 404 | Update a task |
| DELETE | `/tasks/{id}` | 204 or 404 | Delete a task |

## Validation

- `title` is required on creation.
- `priority` must be `low`, `medium` or `high`.
- `status` must be `todo`, `in_progress` or `done`.
- `due_date` must be a date in `YYYY-MM-DD` format.

## Known limitations

- No authentication.
- No persistence.
- No pagination.
