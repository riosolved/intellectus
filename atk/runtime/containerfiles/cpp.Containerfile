# atk-cpp: compiles and runs C++17 challenges. Alpine + g++ is ~250MB
# versus ~1.4GB for the official Debian-based gcc image.
FROM alpine:3.21
RUN apk add --no-cache g++
