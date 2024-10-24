# 99 Group Data Engineering Technical Test

## ELT SQL Pipeline Executor

This project simulates the execution of an ELT (Extract, Load, Transform) data pipeline by running SQL files in the correct order based on their dependencies. The pipeline is divided into three stages:

1. **Source**: Contains the raw data tables.
2. **Tmp**: Contains SQL scripts that clean, transform, and combine data.
3. **Final**: Contains SQL scripts that create the final data mart.

The SQL files are stored in a directory structure that mimics this pipeline:

## Features

- **Dependency Management**: Determines the dependencies of each SQL file by checking references to other tables.
- **Execution Order**: Runs the SQL files in the correct order based on their dependencies.
- **Simulation**: Simulates the execution of SQL files by using a `time.sleep(2)` to represent the time taken to run each file.
- **Commands**:
  - `dependencies`: Prints the dependencies of all SQL files in the `tmp` and `final` directories.
  - `run`: Executes the SQL files in the correct order based on their dependencies.

## Usage

python3 main.py dependencies <sql_directory>
python3 main.py run <sql_directory>

### Prerequisites

- Python 3.x

