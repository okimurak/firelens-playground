# firelens-playground

## requirement

- Java 8
- Terraform
- ecspresso

## container

Build container

```bash
cd docker
docker build -t firelens-sample .
```

## terraform

Create network env.

```bash
cd terraform
terraform plan
terraform apply
```

## ecspresso

Deploy container to ECS.

```bash
ecspresso deploy --config config.yaml
```
