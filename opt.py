from getopt import getopt, GetoptError
from sys import exit

# Argument's name
OPT_PROCESSES = ("-p", "--processes")
OPT_DIFFICULTY = ("-d", "--difficulty")
OPT_HELP = ("-h", "--help")

# Default opt values
DEFAULT_PROCESSES = 1
DEFAULT_DIFFICULT = 4

# Error codes
ERROR_CODE = 1

# Print usage
def usage():
    print(
        "usage: main.py [OPTION]\n" +
        "\n" +
        "This is a program, that demonstrates an example of proof of work algorithm, with parallel execution.\n"
        "\n" +
        "optional arguments:\n" +
        "\t-p, --processes\t\tan integer, specify the number of processes;\n\t\t\t\tdefault %d\n" % (DEFAULT_PROCESSES) +
        "\t-d, --difficulty\tan integer, specify proof of work difficulty;\n\t\t\t\tin this case, it is count of zeroes at the start of the wanted hash;\n\t\t\t\tdefault %d\n" % (DEFAULT_DIFFICULT) +
        "\t--help\t\t\tdisplay this help and exit\n" +
        "\n" +
        "Exit status:\n" +
        "0  if OK,\n" +
        "%d  if some problems\n" % (ERROR_CODE)
    )
    # Exit program
    exit(ERROR_CODE)

# Handle invalid value in the argument.
def optErrorInteger(opt):
    print("Argument %s or %s should be an integer.\n" % (opt[0], opt[1]))
    usage()

# Parse arguments
def optParse(argv):
    # Create a dictionary with default arguments
    arguments = dict(processes_count=DEFAULT_PROCESSES, difficulty=DEFAULT_DIFFICULT)

    try:
        # Call library for parse arguments
        opts, _ = getopt(argv[1:], "p:d:h", ["processes=", "difficulty=", "help"])
    except GetoptError:
        # Print usage if rise some error. The user inserts invalid arguments.
        usage()

    # Handle parsed arguments
    for opt, arg in opts:

        if opt in OPT_HELP:
            usage()
        
        if opt in OPT_PROCESSES:
            try:
                arguments["processes_count"] = int(arg)
            except ValueError:
                optErrorInteger(OPT_PROCESSES)

        if opt in OPT_DIFFICULTY:
            try:
                arguments["difficulty"] = int(arg)
            except ValueError:
                optErrorInteger(OPT_DIFFICULTY)

    # Return a dictionary with arguments.
    return arguments