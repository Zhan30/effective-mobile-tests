# Effective Mobile Automation Tests

This project implements automated tests for
the [Effective Mobile Main Page](https://effective-mobile.ru/). The
tests are written using **Python**, **Pytest**, **Allure** and **Playwright**. The test application’s source code is available
on [GitHub](https://github.com/Zhan30/effective-mobile-tests.git).

## Project Overview

The goal of this project is to complete a test task to automate navigation testing across all blocks of the Effective Mobiles homepage. Automated tests check the corresponding locators and URLs. The project structure utilizes Page Object and Page Factory design patterns.

## Getting Started

### Clone the Repository

To get started, clone the project repository using Git:

```bash
git clone https://github.com/Zhan30/effective-mobile-tests.git
cd effective-mobile-tests
```

### Running the Tests on your computer on Windows

To run the tests on your computer you need to do the following steps:
 
- At first its need to install Docker. Go to the official website: [Docker](https://www.docker.com/products/docker-desktop/).
- Press to button **Download Docker Desktop**
- After downloading run the installation Docker
- After installation type this command in command prompt (CMD, PowerShell or terminal Windows Terminal): 
```bash
docker --version
```
- If everything is working, you can see the Docker version, for example:
```bash
Docker version 24.0.6, build ed223bc
```
- Then run the following command:
```bash
docker build -t effective-mobile-tests .
```
- After building image run the container:
```bash
docker run effective-mobile-tests
```
- After running the tests, delete the container:
```bash
docker rm effective-mobile-tests
```
- And delete the image
```bash
docker rmi effective-mobile-tests
```
