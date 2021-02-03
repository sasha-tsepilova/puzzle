import puzzle

if __name__ == "__main__":
    if puzzle.validate_board(["**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"]) == False:
        print('Everything is ok')
    else:
        print('Something goes wrong')
