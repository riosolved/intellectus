# atk-python: runs Python challenges, solutions, and SQL verification
# scripts (stdlib sqlite3). Exactly alpine, environment set up explicitly.
# The image stays dependency-free: student requirements.txt files are baked
# into derived images (atk-python-deps-<hash>) at run time - see
# runtime/runners/python.py.
FROM alpine:3.21
RUN apk add --no-cache python3 py3-pip
