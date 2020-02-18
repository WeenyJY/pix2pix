import cv2
import os
def create_dir_not_exist(path):
    if not os.path.exists(path):
        os.mkdir(path)
def main():
	i=0
	File_path = r"G:\Dataset\danbooru2018\512px\0003"
	for root, dirs, files in os.walk(File_path):
		for d in dirs:
			print("dirs:\n"+d) #打印子资料夹的个数
		lens=str(len(files))
		for file in files:
			print("files:\n"+file)
			#讀入圖像
			img_path = root+'/'+file
			img_size = 256
			img = cv2.imread(img_path,1) #读入彩色图片 
			img = cv2.resize(img,(img_size,img_size))
			img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #转为灰度图片
			img_gray_RGB = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
			save_path = './val/'
			create_dir_not_exist(save_path) #在当前文件夹内创建保存位置
			img_name = "out_"+file 
			img_save = cv2.resize(img_gray_RGB,(2*img_size,img_size))
			img_save[0:img_size,0:img_size]=img
			img_save[0:img_size,img_size:2*img_size]=img_gray_RGB
			cv2.imwrite(save_path+img_name,img_save)
			i+=1
			# 测试一下
			# if(i>5):
			# 	break
			print(str(i)+"/"+lens)
if __name__ == '__main__':
	main()
