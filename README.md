# Repro for issue 8659

## Versions

firebase-tools: 14.4.0<br>
python: v3.12.4<br>

## Steps to reproduce

1. Install dependencies
   - Run `cd functions/`
   - Run `python3.12 -m venv venv`
   - Run `. ./venv/bin/activate`
   - Run `pip install -r requirements.txt`
2. Open a new terminal, then run `firebase emulators:start --project demo-project`
   - A warning message is raised

```
⚠  Error adding Task Queue function: FirebaseError: Request to http://127.0.0.1:9499/projects/demo-project/locations/us-central1/queues/backup_a_pod had HTTP Error: 400, Queue ID must start with a letter followed by up to 62 letters, numbers, hyphens, or underscores and must end with a letter or a number
```

## Notes

When deploying with `firebase deploy --project`, an error is raised when creating the Cloud Tasks Queue

```
Request to https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/us-central1/queues/backup_a_pod had HTTP Error: 400, Queue ID "backup_a_pod" can contain only letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). Queue ID must be between 1 and 100 characters.

Functions deploy had errors with the following functions:
        backup_a_pod(us-central1)

Error: There was an error deploying functions
```

The warning message from "Steps to reproduce" seems to be misleading as it implies `underscores` are allowed
