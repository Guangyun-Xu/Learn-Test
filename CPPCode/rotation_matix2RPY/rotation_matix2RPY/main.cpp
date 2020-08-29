#include <iostream>
#include <Eigen/Core>
#include <Eigen/Geometry>
#include <math.h>

int main()
{
    Eigen::Matrix3f rotationMatrix;
    rotationMatrix <<
                      -0.0101817,	-0.999944,	 0.00300482,
                      0.985716,	-0.00953149,	0.168148,
                      0.16811,	   -0.00467393,	 -0.985757;
    //旋转矩阵转换为欧拉角
    //ZYX顺序，即先绕x轴roll,再绕y轴pitch,最后绕z轴yaw,0表示X轴,1表示Y轴,2表示Z轴
    //参考:https://blog.csdn.net/weicao1990/article/details/86148828
    Eigen::Vector3f euler_angles = rotationMatrix.eulerAngles(2, 1, 0);
    std::cout<<euler_angles<<std::endl;
    std::cout << "yaw(x) pitch(y) roll(z) = " << 180.0f*euler_angles.transpose()/3.14f << std::endl;

}


