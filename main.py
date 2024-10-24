import re
import os
import time
import argparse
import sys

from collections import defaultdict, deque

#for finding and extracting the dependencies
def checkDependencies(sqlFile):
    pattern = r'`([a-zA-Z0-9_]+.[a-zA-Z0-9_]+)`'
    return re.findall(pattern, sqlFile)

def process(directory):
    dependencies = defaultdict(set)

    for folder in ['tmp', 'final']:
        folder_path = os.path.join(directory, folder)
        for filename in os.listdir(folder_path):
            if filename.endswith('.sql'):
                with open(os.path.join(folder_path, filename), 'r') as file:
                    sqlFile = file.read()
                    deps = checkDependencies(sqlFile)
                    for dep in deps:
                        dependencies[filename].add(dep)

    return dependencies

def sortDependencies(dependencies):
    inDegree = {file: 0 for file in dependencies}
    for deps in dependencies.values():
        for dep in deps:
            if dep not in inDegree:
                inDegree[dep] = 0  
            inDegree[dep] += 1

    queue = deque([file for file, degree in inDegree.items() if degree == 0])
    sortedFile = []

    while queue:
        currFile = queue.popleft()
        sortedFile.append(currFile)

        for dependent in dependencies[currFile]:
            inDegree[dependent] -= 1
            if inDegree[dependent] == 0:
                queue.append(dependent)

    return sortedFile


def simulate(file):
    time.sleep(2)  # Simulate running the SQL file
    print(f"Executed: {file}")



def getDependencies(directory):
    dependencies = process(directory)

    for sql_file, deps in dependencies.items():
        print(f"\nFile Name: {sql_file}")
        print("Dependencies:")
        for dep in deps:
            print(f"- {dep}")
    print()

def run(directory):
    dependencies = process(directory)
    run_order = sortDependencies(dependencies)

    print("Run Order:")
    for sql_file in run_order:
        print(f" - {sql_file}")
        simulate(sql_file)



def print_help():
    print(
        """Usage: {} <command> <directory>\n
Available commands:
  dependencies  Show the dependencies of SQL files
  run           Execute SQL files in the correct order\n
Example:
  {} dependencies data-engrg-test-main/sql
  {} run data-engrg-test-main/sql
        """.format(
            sys.argv[0], sys.argv[0], sys.argv[0]
        )
    )

VALID_CMDS = {
    "dependencies" : lambda: getDependencies,
    "run" : lambda: run
}



# Map commands to functions
VALID_CMDS = {
    "dependencies": getDependencies,
    "run": run
}

def main():
    if len(sys.argv) != 3:
        print_help()
        return

    cmd = sys.argv[1]
    directory = sys.argv[2]

    if not os.path.exists(directory):
        print(f"Error: directory '{directory}' does not exist\n")
        return

    if cmd not in VALID_CMDS:
        print('Error: invalid command\n')
        print_help()
        return

    # Call the correct function with the directory argument
    VALID_CMDS[cmd](directory)

if __name__ == '__main__':
    main()



