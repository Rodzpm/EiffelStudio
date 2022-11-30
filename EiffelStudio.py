#IMPORTS
import sys

def main():
    #4 modes:
    #   - mode playground (-p)
    #   - mode enregistrement (-r "sound_name")
    #   - mode lecture (-l "sound_file")
    #   - mode export (-e "sound_file")

    args = sys.argv
    if args[1] == "-p" and len(args) == 2:
        from options.playground import playground
        playground()
    if args[1] == "-r" and len(args) == 3:
        from options.record import record
        record(args[2])
    if args[1] == "-l" and len(args) == 3:
        from options.listen_music import listen_music
        listen_music(args[2])
    if args[1] == "-e" and len(args) == 3:
        from options.export import export
        export(args[2])

if "__main__" == __name__:
    main()