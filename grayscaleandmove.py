"ディレクトリsys.argv[1]にある画像ファイル(拡張子はsys.argv[2])を"
"連番6桁のファイル名「??????.(拡張子)」に変更してsys.argv[3]に移動"
"連番の開始番号:sys.argv[4]"

#グレースケール化も可能()
#グレースケール化にはopenCVを使用
import sys
import cv2
import glob
import os

if __name__=='__main__':
    filelist=glob.glob(sys.argv[1]+'/*.'+sys.argv[2])
    gccount=0#グレースケール化した枚数
    
    print("GRAYSCALE?(Yes=1,No=0)")
    mode=2
    while(mode!=0 and mode!=1):
        mode=input()#グレースケール化する(1)かしないか(0)

    for i,file in enumerate(filelist):
        i_str=str(i+int(sys.argv[4])).zfill(6)#連番6桁化
        if mode==1:#グレースケール化する場合のみ以下の処理をする
            img=cv2.imread(file)
            img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            cv2.imwrite(file,img)
            gccount+=1

        os.rename(file,sys.argv[3]+i_str+sys.argv[2])#移動
    
    print("Completed!")
    print("GRAYSCALE/TOTAL={}/{}".format(gccount,len(filelist)))

            

