# """
# String literals can span multiple lines. 
# One way is using triple-quotes: " " " ..." " "  or ' ' '...' ' '. 
# End of lines are automatically included in the string, 
# but it’s possible to prevent this by adding a \ at the end of the line. 
# The following example:
# """

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

"""  出力結果： note that the initial newline is not included
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to

"""