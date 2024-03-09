import os
import subprocess

while True:
    command = input("$ ")

    # Check for IO redirection
    input_file = None
    output_file = None

    if '<' in command:
        command_parts = command.split('<')
        command = command_parts[0].strip()
        input_file = command_parts[1].strip()

    if '>' in command:
        command_parts = command.split('>')
        command = command_parts[0].strip()
        output_file = command_parts[1].strip()

    # Execute the command
    if '|' in command:
        # Handle piped commands
        commands = command.split('|')
        previous_output = None

        for cmd in commands:
            cmd = cmd.strip()

            if previous_output:
                process = subprocess.Popen(cmd, shell=True, stdin=previous_output.stdout, stdout=subprocess.PIPE)
                previous_output.stdout.close()
            else:
                process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

            previous_output = process

        output, _ = process.communicate()
        print(output.decode().strip())
    else:
        # Execute a single command
        if input_file:
            with open(input_file, 'r') as file:
                process = subprocess.Popen(command, shell=True, stdin=file, stdout=subprocess.PIPE)
        else:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

        output, _ = process.communicate()
        print(output.decode().strip())

    # Write output to file if necessary
    if output_file:
        with open(output_file, 'w') as file:
            file.write(output.decode().strip())