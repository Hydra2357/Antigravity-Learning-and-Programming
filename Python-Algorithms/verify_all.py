"""
Algorithm Verification Runner
Finds all algorithm Python files in subdirectories and executes them
to ensure they are syntactically and logically correct.
"""

import os
import sys
import subprocess

def main():
    workspace_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Algorithm Verification Runner starting in: {workspace_dir}\n")
    
    # Track results
    success_count = 0
    failure_count = 0
    failures = []
    
    # Gather all Python files, grouped by directory
    for root, dirs, files in sorted(os.walk(workspace_dir)):
        # Skip the root directory itself to not run verify_all.py recursively
        if root == workspace_dir:
            continue
            
        py_files = [f for f in files if f.endswith('.py')]
        if not py_files:
            continue
            
        rel_dir = os.path.relpath(root, workspace_dir)
        print(f"=== Running tests in folder: {rel_dir} ===")
        
        for file in sorted(py_files):
            file_path = os.path.join(root, file)
            rel_file_path = os.path.relpath(file_path, workspace_dir)
            
            print(f"  Running {file:.<35} ", end="", flush=True)
            
            try:
                # Run the python script in a subprocess
                result = subprocess.run(
                    [sys.executable, file_path],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=10 # 10 seconds timeout per script
                )
                
                if result.returncode == 0:
                    print("[ SUCCESS ]")
                    success_count += 1
                else:
                    print("[ FAILURE ]")
                    print(f"\n--- Stderr from {rel_file_path} ---")
                    print(result.stderr)
                    print("-" * 40)
                    failure_count += 1
                    failures.append(rel_file_path)
            except subprocess.TimeoutExpired:
                print("[ TIMEOUT ]")
                failure_count += 1
                failures.append(rel_file_path)
            except Exception as e:
                print(f"[ ERROR: {e} ]")
                failure_count += 1
                failures.append(rel_file_path)
                
        print() # blank line between directories
        
    print("=== Verification Summary ===")
    print(f"Total Successful runs: {success_count}")
    print(f"Total Failures:        {failure_count}")
    
    if failure_count > 0:
        print("\nFailed files:")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    else:
        print("\nAll algorithms verified successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
