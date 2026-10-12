# Databricks Asset Bundles (DAB) – Customer Data Pipeline

## Project Overview

This project demonstrates how to develop, configure, and deploy Databricks data engineering resources using **Databricks Asset Bundles (DAB)** and the Databricks CLI.

The project follows a Bronze–Silver–Gold data processing architecture and uses YAML-based configuration to manage Databricks resources as code.

The main objective is to make deployment repeatable, maintainable, and suitable for development and production environments.

## Tech Stack

- **Data Engineering:** Databricks, Apache Spark, PySpark
- **Data Processing:** Delta Lake, Bronze–Silver–Gold architecture
- **Deployment:** Databricks Asset Bundles (DAB)
- **Configuration:** YAML
- **Version Control:** Git and GitHub
- **Cloud Storage:** AWS S3
- **CLI:** Databricks CLI

## Architecture

```text
          AWS S3
      Customer Source Data
              |
              v
      Databricks Workspace
              |
              v
     Databricks Asset Bundle
        databricks.yml
              |
       +------+------+
       |             |
       v             v
   Resources       Source Code
   YAML Files      PySpark
       |             |
       +------+------+
              |
              v
        Databricks Job
              |
              v
        Bronze Layer
       Raw Customer Data
              |
              v
         Silver Layer
    Cleaned and Validated Data
              |
              v
          Gold Layer
    Business-Ready Data
```

## Key Features

### 1. Infrastructure and Resources as Code

Used Databricks Asset Bundles to define and manage Databricks resources through configuration files instead of creating every resource manually in the workspace.

### 2. YAML-Based Configuration

Used `databricks.yml` as the main configuration file to define the bundle, include resource definitions, configure variables, and manage deployment targets.

### 3. Resource Management

Organized Databricks job and pipeline definitions into separate YAML files under the `resources/` directory for better maintainability and reusability.

### 4. Environment-Based Deployment

Configured deployment targets such as development and production to manage environment-specific settings.

### 5. Bronze–Silver–Gold Data Processing

Designed the customer data pipeline using a layered architecture:

- **Bronze:** Ingest raw customer data from AWS S3.
- **Silver:** Clean, validate, and transform customer records.
- **Gold:** Prepare business-ready data for analytics and reporting.

### 6. Databricks CLI Deployment

Used Databricks CLI commands to validate the bundle, deploy resources to the workspace, and execute the configured job.

### 7. Git-Based Version Control

Managed project files through Git and GitHub to maintain code history and support collaborative development.

### 8. CI/CD Readiness

Structured the project to support automated validation and deployment using CI/CD tools such as GitHub Actions or Azure DevOps.

## Project Structure

```text
customer-project/
│
├── databricks.yml
│
├── resources/
│   ├── jobs.yml
│   └── pipelines.yml
│
├── src/
│   └── customer/
│       ├── bronze.py
│       ├── silver.py
│       └── gold.py
│
├── tests/
│
├── .gitignore
└── README.md
```

*Note: Adjust the file names and folders to match your actual repository.*

## How Databricks Asset Bundles Work

1. Define Databricks resources in YAML configuration files.
2. Store notebooks and source code in the project directory.
3. Configure workspace and environment-specific settings in `databricks.yml`.
4. Validate the bundle configuration using the Databricks CLI.
5. Deploy the bundle to the selected Databricks workspace.
6. Run the deployed job and monitor its execution.

## How to Run the Project

### Prerequisites

- Databricks workspace
- Databricks CLI installed
- Python and PySpark development environment, as required by the project
- AWS S3 access, if required by the pipeline
- Git

### Step 1: Authenticate with Databricks

Configure the Databricks CLI authentication for your workspace.

```bash
databricks auth login --host <DATABRICKS_WORKSPACE_URL>
```

### Step 2: Navigate to the Project

```bash
cd customer-project
```

### Step 3: Validate the Bundle

```bash
databricks bundle validate -t dev
```

### Step 4: Deploy to Development

```bash
databricks bundle deploy -t dev
```

### Step 5: Run the Job

Replace `customer_job` with the actual job resource key defined in your bundle.

```bash
databricks bundle run -t dev customer_job
```

### Step 6: Deploy to Production

After testing and approval, deploy using the configured production target.

```bash
databricks bundle validate -t prod
databricks bundle deploy -t prod
```

**Note:** The `dev` and `prod` targets must be configured in `databricks.yml`. Production deployment should follow your organization's approval and access-control process.

## Important DAB Commands

| Command | Purpose |
|---|---|
| `databricks bundle init` | Initialize a bundle from a template |
| `databricks bundle validate -t dev` | Validate configuration for development |
| `databricks bundle deploy -t dev` | Deploy resources to development |
| `databricks bundle run -t dev customer_job` | Run the configured job |
| `databricks bundle summary -t dev` | View deployed bundle resource information |
| `databricks bundle destroy -t dev` | Remove bundle-managed resources; use with caution |

## Skills Demonstrated

- Databricks Asset Bundles
- Databricks CLI
- YAML configuration
- PySpark and Delta Lake
- AWS S3 integration
- Bronze–Silver–Gold architecture
- Job and pipeline resource management
- Environment-specific deployment
- Git and GitHub
- CI/CD concepts and deployment automation

## Future Enhancements

- Implement automated CI/CD using GitHub Actions.
- Add automated data quality tests.
- Add logging, monitoring, and failure notifications.
- Introduce separate staging and production environments.
- Add deployment approvals and environment-specific permissions.

## Author

**Rajneekant Malavadkar**

Data Engineer | AWS | Databricks | PySpark | SQL | Delta Lake | DAB | dbt | Snowflake


