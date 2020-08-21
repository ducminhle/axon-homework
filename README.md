Axon Homework

# CI
* This project uses Jenkins service to run CI
* We need to config Multibranch Pipeline with ci/Jenkinsfile config file.
* CI strategy has 3 stages to build and deploy on dev environment:
```
- When developers create pull requests, Jenkins will run unit tests, code coverage. If code coverage pass, this pull request can be merged.
- After merged, this project will be build Docker image and push the image to Docker repository.
- If build success, application will be deployed to dev environment with Helm Charts has been config in ci folder.
- After deployed success, we can setup run an integration test, if report is good CI result is success else revert commit.
```

# Handle zero downtime
- The application need to support readinessProbe and livenessProbe.
- Config strategy with type RollingUpdate and set maxUnavailable: 0.
- Config Horizontal Pod Autoscaler (to easy config HPA, we can use banzaicloud/hpa-operator) to make sure all service will be not crash when we upgrade.