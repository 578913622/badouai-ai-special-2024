import numpy as np
import cv2

#调用接口
# cv2.resize(img, (800,800,c),near/bin)  near/bin为选择最临近插值或双线性插值，伪代码
#本质是求虚拟点的像素值
#手写方法
def bilinear_interpolation(img,out_dim):
    src_h, src_w, channel = img.shape
    dst_h, dst_w = out_dim[0],out_dim[1]
    print("src_h,src_w ",src_h,src_w)
    print("dst_h,dst_w",dst_h,dst_w)
    if src_h == dst_h and src_w == dst_w:
        return img.copy()
    dst_img = np.zeros((dst_h,dst_w,3),dtype=np.uint8)
    scale_x,scale_y = float(src_w)/dst_w,float(src_h)/dst_h #计算缩放比例

    for i in range(channel):
        for dst_y in range(dst_h):
            for dst_x in range(dst_w):
                #运用假设法，找到一个数值使中心点加上该数值后与目标图的中心点相同,中心对称法
                src_x = (dst_x + 0.5) * scale_x - 0.5
                src_y = (dst_y + 0.5) * scale_y - 0.5

                #对边界的处理
                src_x0 = int(np.floor(src_x)) #np.floor()返回不大于输入参数的最大整数。（向下取整）
                src_x1 = min(src_x0 + 1, src_w - 1)
                src_y0 = int(np.floor(src_y))
                src_y1 = min(src_y0 + 1, src_h - 1)

                #计算结果
                temp0 = (src_x1 - src_x) * img[src_y0,src_x0,i] + (src_x - src_x0) * img[src_y0,src_x1,i]
                temp1 = (src_x1 - src_x) * img[src_y1,src_x0,i] + (src_x - src_x0) * img[src_y1,src_x1,i]
                dst_img[dst_y,dst_x,i] = int((src_y1 - src_y) * temp0 + (src_y - src_y0) * temp1)

    return dst_img

if __name__ == '__main__':
    img = cv2.imread("lenna.png")
    dst = bilinear_interpolation(img,(700,700))
    cv2.imshow('bilinear_interpolation',dst)
    cv2.waitKey(0)
    cv2.destroyWindow()
