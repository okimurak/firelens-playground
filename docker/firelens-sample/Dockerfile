FROM java:8-jdk-alpine as builder
COPY src/Main.java /usr/src/myapp/Main.java
WORKDIR /usr/src/myapp
RUN javac Main.java

FROM java:8-jre-alpine as runner
COPY --from=builder /usr/src/myapp/Main.class /usr/src/myapp/Main.class
COPY entrypoint.sh /usr/src/myapp/entrypoint.sh
RUN chmod +x /usr/src/myapp/entrypoint.sh
WORKDIR /usr/src/myapp
ENTRYPOINT [ "/usr/src/myapp/entrypoint.sh" ]