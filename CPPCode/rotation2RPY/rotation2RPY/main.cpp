#include <iostream>
#include <Eigen/Core>
#include <Eigen/Geometry>
#include <math.h>

void direction2RotationMatrix(const Eigen::Vector3f suctionDirectin,
                              Eigen::Matrix3f &rotationMatrix);

int main()
{
    Eigen::Matrix3f rotationMatrix;

    Eigen::Vector3f suctionDirectin(0.45611f, 0.0118419f, -0.889845f);

    direction2RotationMatrix(suctionDirectin, rotationMatrix);

    std::cout<< "rotation matrix:\n" << rotationMatrix <<std::endl;
    //旋转矩阵转换为欧拉角
    //ZYX顺序，即先绕x轴roll,再绕y轴pitch,最后绕z轴yaw,0表示X轴,1表示Y轴,2表示Z轴
    //参考:https://blog.csdn.net/weicao1990/article/details/86148828
    Eigen::Vector3f euler_angles = rotationMatrix.eulerAngles(2, 1, 0);

    std::cout << "yaw(z) pitch(y) roll(x) = " << 180.0f*euler_angles.transpose()/3.14f << std::endl;



    return 0;
}

void direction2RotationMatrix(const Eigen::Vector3f suctionDirectin,
                              Eigen::Matrix3f &rotationMatrix)
{
    rotationMatrix(0,2) = suctionDirectin[0];
    rotationMatrix(1,2) = suctionDirectin[1];
    rotationMatrix(2,2) = suctionDirectin[2];

    float a = (float)sqrt(pow(suctionDirectin[0],2)+pow(suctionDirectin[1],2));
    rotationMatrix(0,1) = (float)suctionDirectin[1]/a;
    rotationMatrix(1,1) = (float)-1.0f*suctionDirectin[0]/a;
    rotationMatrix(2,1) = 0.0f;

    rotationMatrix(0,0) =(float)(-1.0f*suctionDirectin[0]*suctionDirectin[2])/a;
    rotationMatrix(1,0) =(float)(-1.0f*suctionDirectin[1]*suctionDirectin[2])/a;
    rotationMatrix(2,0) =(float)(pow(suctionDirectin[0], 2)+pow(suctionDirectin[1], 2))/a;

}

