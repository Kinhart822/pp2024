import subprocess
import shlex

def execute_command(command):
    try:
        args = shlex.split(command)
        
        input_redirect = None
        output_redirect = None
        if '<' in args:
            input_index = args.index('<')
            input_redirect = args[input_index + 1]
            args = args[:input_index]
        if '>' in args:
            output_index = args.index('>')
            output_redirect = args[output_index + 1]
            args = args[:output_index]

        # Execute the main task
        if input_redirect and output_redirect:
            with open(input_redirect, 'r') as f_in, open(output_redirect, 'w') as f_out:
                process = subprocess.Popen(args, stdin=f_in, stdout=f_out, stderr=subprocess.PIPE)
        elif input_redirect:
            with open(input_redirect, 'r') as f_in:
                process = subprocess.Popen(args, stdin=f_in, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif output_redirect:
            with open(output_redirect, 'w') as f_out:
                process = subprocess.Popen(args, stdout=f_out, stderr=subprocess.PIPE)
        else:
            process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Read output from the process
        output, error = process.communicate()

        # Print output and error message 
        if output:
            print(output.decode())
        if error:
            print(error.decode())
    except Exception as e:
        print(f"Error: {e}")

def shell():
    with open('output.txt', 'w') as f:
        while True:
            try:
                command = input("$ ")
                f.write(f"$ {command}\n")
                if command.lower() == 'exit':
                    break
                execute_command(command)
            except KeyboardInterrupt:
                print("\nExiting...")
                break

if __name__ == "__main__":
    shell()
