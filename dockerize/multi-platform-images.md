You can have both amd64 and arm64 images to have the same name (tag) in AWS ECR by utilizing a multi-architecture image setup. This is achieved through the use of a manifest list, which allows you to reference multiple architectures under a single image name (or tag). When a user or a system pulls the image from the registry, the Docker client or any compatible container runtime automatically selects the appropriate architecture version of the image based on the architecture of the host system.

This approach doesn't require you to manage separate tags for different architectures explicitly. Instead, you create and push individual images for each architecture to your repository and then create a manifest list that references these images. The manifest list is then pushed to the registry under the shared tag name. This shared tag acts as a pointer to the correct architecture-specific image.

Here's a simplified overview of how to accomplish this:

Build the architecture-specific images: You need to build your Docker images for each target architecture. Ensure each image is built correctly for its intended architecture (amd64, arm64, etc.).

Push the architecture-specific images to ECR: Push these images to your AWS ECR repository. Even though these images are pushed to the repository, you typically don't access them directly with separate tags at this point.

Create a multi-architecture manifest: Using Docker CLI's manifest command (or Docker Buildx, which provides more extensive support for building multi-arch images), you can create a manifest list. This list includes references to the architecture-specific images you've pushed to the repository.

Push the manifest list to ECR under a common tag: This tag is what users will use to pull the image. The container runtime automatically resolves which architecture-specific image to pull based on the host's architecture.

Here is a brief example using Docker commands:

Tag your image so you can push the image to this repository:

```
docker tag kedematcher-image:latest public.ecr.aws/kedehub/kedematcher-image:arm64-latest
```

```
docker tag kedematcher-image:latest public.ecr.aws/kedehub/kedematcher-image:amd64-latest
```

First, you would push your architecture-specific images to ECR (assuming you've already built them):

``` 
docker push public.ecr.aws/kedehub/kedematcher-image:arm64-latest
```

```
docker push public.ecr.aws/kedehub/kedematcher-image:amd64-latest
```

Then, create and push a manifest list that references both images under a shared tag:

```
docker manifest create public.ecr.aws/kedehub/kedematcher-image:latest public.ecr.aws/kedehub/kedematcher-image:arm64-latest public.ecr.aws/kedehub/kedematcher-image:amd64-latest
```

```
docker manifest push public.ecr.aws/kedehub/kedematcher-image:latest
```

This way, when a user pulls the image from the registry, the Docker client or any compatible container runtime automatically selects the appropriate architecture version of the image based on the architecture of the host system.

