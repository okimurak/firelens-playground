# firelens-playground

## requirement

- Java 8
- Terraform
- Docker
- Docker-compose

## container

Build container

```bash
cd docker
docker-compose build
```

Run container

```bash
cd docker
docker-compose up
```

## terraform

Create network env.

```bash
cd terraform
terraform plan
terraform apply
```

## ecspresso

Update task definiton to ECS.

```bash
ecspresso register --config config.yaml
```
