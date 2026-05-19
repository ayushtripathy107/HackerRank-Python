if __name__ == '__main__':
    N = int(input())
    res = []
    
    for _ in range(N):
        # Read the command and split it into parts
        command_parts = input().split()
        cmd = command_parts[0]
        
        if cmd == "insert":
            res.insert(int(command_parts[1]), int(command_parts[2]))
        elif cmd == "print":
            print(res)
        elif cmd == "remove":
            res.remove(int(command_parts[1]))
        elif cmd == "append":
            res.append(int(command_parts[1]))
        elif cmd == "sort":
            res.sort()
        elif cmd == "pop":
            res.pop()
        elif cmd == "reverse":
            res.reverse()
