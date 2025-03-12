def TOH(disk,source,extra,target):
    if (disk == 1):
        print("Move disk from rod {} to rod {}".format (source,target))
        return
    
    TOH(disk-1,source,target,extra)
    print("Move disk {} from rod {} to rod {}".format (disk,source,target))
    TOH(disk-1,source,extra,target)

disks=int(input("Enter the number of disk: "))
TOH(disks,'A','B','C')
