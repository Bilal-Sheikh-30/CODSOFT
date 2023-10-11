import json
def saveList(taskList):
    with open('task.txt', 'w') as file:
        json.dump(taskList, file)
    return
def firstInterface():
    print('''
Select operation:
1. Show list
2. Create new list
3. Exit''')
    with open('task.txt') as file:
        # grandTaskList is the normal dict containing mega record of task lists
        grandTaskList = {}
        jsonTaskList = json.load(file)

    # converting json dict into normal dict
    for item in jsonTaskList:
        grandTaskList[item] = jsonTaskList[item]
    firstInterfaceChoice = int(input('>> '))
    if firstInterfaceChoice == 1:
        keylist = list(grandTaskList)
        print()
        for i in range(len(keylist)):
            print(f'{i+1}. {keylist[i]}')
        listNo = int(input('Enter list# to view list item: '))
        if listNo > 0 and listNo <= len(keylist):
            # selectedTaskList => user selected list containing tasks
            selectedTaskList = grandTaskList.get(keylist[listNo - 1])
            print()
            for task in range(len(selectedTaskList)):
                print(f'{task + 1}. {selectedTaskList[task]}')
            updateConfirmation = input('\nDo you want to update list? (y / n)').lower()
            if updateConfirmation == 'y':
                actionType = input('\nEnter "a" to add another task and serial# to marked complete a task: ')
                if actionType == 'a' or actionType == 'A':
                    print('\nEnter "e" when you have entered all tasks')
                    while True:
                        newTask = input('>> ')
                        if newTask == 'e' or newTask == 'E':
                            break
                        else:
                            selectedTaskList.append(newTask)
                    grandTaskList[keylist[listNo - 1]] = selectedTaskList
                    print('Your list has been updated\n')
                    print(str(keylist[listNo - 1]).capitalize())
                    for task in range(len(selectedTaskList)):
                        print(f'{task + 1}. {selectedTaskList[task]}')
                    saveList(grandTaskList)
                elif actionType.isalpha() and (actionType != 'a' or actionType != 'A'):
                    print('Invalid input')

                elif 0 < int(actionType) <= len(selectedTaskList):
                    selectedTaskList.pop(int(actionType) - 1)
                    print('\nAction Completed\n')
                    print(str(keylist[listNo - 1]).capitalize())
                    for task in range(len(selectedTaskList)):
                        print(f'{task + 1}. {selectedTaskList[task]}')
                    grandTaskList[keylist[listNo - 1]] = selectedTaskList
                    saveList(grandTaskList)
                elif 0 > int(actionType) > len(selectedTaskList):
                    print('Invalid input')
            else:
                firstInterface()


        else:
            return
    elif firstInterfaceChoice == 2:
        newListTitle = input('Enter list title: ')
        print('\nEnter "e" when you have entered all tasks')
        newTaskList = []
        while True:
            newTask = input('>> ')
            if newTask == 'E' or newTask == 'e':
                break
            else:
                newTaskList.append(newTask)
        print('\n Your list has been created')
        grandTaskList[newListTitle] = newTaskList
        print(newListTitle)
        for task in range(len(newTaskList)):
            print(f'{task + 1}. {newTaskList[task]}')
        saveList(grandTaskList)

    elif firstInterfaceChoice == 3:
        return
    else:
        firstInterface()
firstInterface()