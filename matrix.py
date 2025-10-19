print("Matrix A")
maRow = int(input("Number of rows "))
maColumn = int(input("Number of columns "))
aMatrix = []

print("Matrix B")
mbRow = int(input("Number of rows "))
mbColumn = int(input("Number of columns "))
bMatrix = []

addResultM = []
subResultM = []


class Entry:
    def __init__(self, row, column, value, name):
        self.row = row
        self.column = column
        self.value = value
        self.name = name


def createMatrix(row_num, column_num, mList, letter):

    i = 0
    j = 0

    while i < row_num:
        i += 1

        row = []

        while j < column_num:
            j += 1
            value = float(input(f"value for {letter}{i}{j} "))
            name = f"{letter}{i}{j}"

            entry = Entry(i, j, value, name)
            row.append(entry)

        j = 0

        mList.append(row)
        row = []


def showMatrix(column_num, mList, letter):
    print(f"Matrix {letter}")
    for row in mList:
        row_info = ""
        i = 0
        while i < column_num:
            row_info += f" | {row[i].name} {row[i].value} | "
            i += 1
        print(row_info)


def addMatrix():
    print("Add")
    if maRow == mbRow and maColumn == mbColumn:
        i = 0
        print("Can Add")
        while i < maRow:
            j = 0
            row = []

            while j < maColumn:

                value = aMatrix[i][j].value + bMatrix[i][j].value
                name = f"c{i+1}{j+1}"

                entry = Entry(i + 1, j + 1, value, name)
                row.append(entry)

                j += 1
            addResultM.append(row)
            row = []

            i += 1

    else:
        print("Can't Add")


def substractMatrix(minuend, subtrahend):
    print("Substract")
    if maRow == mbRow and maColumn == mbColumn:
        i = 0
        print("Can Substract")
        while i < maRow:
            j = 0
            row = []

            while j < maColumn:

                value = minuend[i][j].value - subtrahend[i][j].value
                name = f"d{i+1}{j+1}"

                entry = Entry(i + 1, j + 1, value, name)
                row.append(entry)

                j += 1
            subResultM.append(row)
            row = []

            i += 1

    else:
        print("Can't Substract")


createMatrix(maRow, maColumn, aMatrix, "a")
createMatrix(mbRow, mbColumn, bMatrix, "b")


showMatrix(maColumn, aMatrix, "A")
showMatrix(mbColumn, bMatrix, "B")
addMatrix()
showMatrix(maColumn, addResultM, "C")
substractMatrix(aMatrix, bMatrix)
showMatrix(maColumn, subResultM, "D")


# loops
# set, dict, list, tuple
