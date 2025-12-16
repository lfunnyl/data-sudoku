def sudoku_validator(grid):
    # Eşittir (=) işaretini koyduğumuzdan emin olalım:
    valid_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # 1. ADIM: SATIRLARI (ROWS) KONTROL ET
    for row in grid:
        if set(row) != valid_set:
            return False

    # 2. ADIM: SÜTUNLARI (COLUMNS) KONTROL ET
    for j in range(9):
        column = []
        for i in range(9):
            column.append(grid[i][j])
        
        if set(column) != valid_set:
            return False

    # 3. ADIM: 3x3 KARELERİ KONTROL ET
    # Tabloyu 3'er 3'er atlayarak geziyoruz (0, 3, 6)
    # i ve j, her bir 3x3'lük bloğun sol üst köşesidir.
    for i in range(0, 9, 3): 
        for j in range(0, 9, 3):
            square = []
            # Şimdi o bloğun içindeki 3x3 alanı tarıyoruz
            for x in range(3):
                for y in range(3):
                    square.append(grid[i+x][j+y])
            
            if set(square) != valid_set:
                return False

    return True