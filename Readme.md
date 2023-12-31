## Example CI/CD pipeline with CircleCI

### Author: RafaelTorices

This repository contains an example of a CI/CD pipeline with CircleCI for a simple Python application (https://github.com/RafaTorices/pycalculator).

## CI/CD pipeline

The CI/CD pipeline is created using CircleCI. The pipeline definition is in the **.circleci/config.yml** file.
For use the pipeline, you need to create a project in CircleCI (<https://app.circleci.com/>) and link it to the repository Github.

In resume, the pipeline has the following steps:

- **Executors**: docker
- **Jobs**:

  - **app-build**: Build the application.
  - **app-test**: Testing the application.
  - **app-docs**: Generate the documentation of the application.
  - **app-release**: Release the application.
  - **app-deploy**: Deploy the application.

- **workflows**: app-workflow

  - **app-build**: Build the application.
  - **app-test**: Requires build. Test the application.
  - **app-docs**: Requires build. Generate the documentation of the application.
  - **app-release**: Requires build, test and docs. Release the application.
  - **app-deploy**: Requires build. Deploy the application.

- **artifacts**: Generated by the jobs.

  - **app-test**: The test coverage xml and html of the application for testing.
  - **app-docs**: The documentation html of the application for review.
  - **app-release**: The package tar.gz of the application for distribution.
  - **app-deploy**: The package dockerhub of the application for upload to DockerHub.

- **orbs**: Used in the pipeline:
  - **SonarCloud**: For the static code analysis.
  - **GitGuardian**: For the secrets detection.

The pipeline is triggered when:

- Commit is made to the **develop** branch
- Commit is made to the **release** branch
- Commit is made to the **main** branch.

The pipeline generates the following artifacts:

- Docker image of the application in DockerHub: <https://hub.docker.com/repository/docker/rafacv99/pycalculator/general>

> #### Note (DockerHub)
>
> The pipeline contains a job for the upload of the docker image to DockerHub. For use the job, you need to create a repository in DockerHub (<https://hub.docker.com/>) and you need to create a token in DockerHub and add it to the CircleCI environment variables with the name DOCKERHUB_PASS and used in the pipeline for generate the artifact.

> #### Note (SonarCloud)
>
> The pipeline contains a job for the static code analysis using SonarCloud and use the SonarCloud Orb. For use the SonarCloud Orb, you need to create a project in SonarCloud (<https://sonarcloud.io/>) and link it to the repository Github. Also, you need to create a token in SonarCloud and add it to the CircleCI environment variables with the name SONAR_TOKEN. The context must be indicated in the workflow jobs. Also, you need to configure the file sonar-project-properties with parameters of the project in SonarCloud.
