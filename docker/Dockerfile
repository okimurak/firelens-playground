FROM openjdk:7
COPY src/Main.java /usr/src/myapp/Main.java
WORKDIR /usr/src/myapp
RUN javac Main.java
COPY entrypoint.sh /usr/src/myapp/entrypoint.sh 
ENTRYPOINT [ "/usr/src/myapp/entrypoint.sh" ]