Attribute VB_Name = "Module1"
Sub stocks()

    output = 2
    lastrow = Cells(Rows.Count, 1).End(xlUp).Row

    For i = 2 To lastrow
        ticker = Cells(i, 1).Value
        nextticker = Cells(i + 1, 1).Value
        vol = Cells(i, 7).Value
        
        If ticker = nextticker Then
            totalsum = totalsum + vol
        
        Else
            totalsum = totalsum + vol
            Cells(output, 10).Value = totalsum
            Cells(output, 9).Value = ticker
            totalsum = 0
            output = output + 1
        
        End If
        
    Next i

End Sub
