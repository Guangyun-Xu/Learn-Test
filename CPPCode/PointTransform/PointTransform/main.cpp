#include "pcl/point_cloud.h"
#include "pcl/point_types.h"
#include "Eigen/Eigen"
#include "Eigen/Geometry"
#include <pcl/common/transforms.h>
#include <cmath>




int main()
{
    // 设置需要变换的点
    pcl::PointXYZ suctionPoint, suctionDirection;
    pcl::PointXYZ startPoint, endPoint;

    suctionPoint.x = -57.8107f;
    suctionPoint.y = -110.266f;
    suctionPoint.z = 1269.81f;

    suctionDirection.x = -0.157574f;
    suctionDirection.y = -0.0184271f;
    suctionDirection.z = -0.987335f;

    startPoint = suctionPoint;
    std::cout<<"startPoint:"<<startPoint<<"\n"<<std::endl;
    endPoint.x = suctionPoint.x + 10.0f*suctionDirection.x;
    endPoint.y = suctionPoint.y + 10.0f*suctionDirection.y;
    endPoint.z = suctionPoint.z + 10.0f*suctionDirection.z;

    //将RPY角转换为旋转矩阵
    double roll = (180.201601694487/180.0)*M_PI;
    double pitch = (8.29690648714927/180.0)*M_PI;
    double yaw = (270.686570091519/180.0)*M_PI;
    Eigen::Matrix3d Rx = Eigen::Matrix3d::Identity();
    Eigen::Matrix3d Ry = Eigen::Matrix3d::Identity();
    Eigen::Matrix3d Rz = Eigen::Matrix3d::Identity();

    Rx (1,1) = cos(roll);
    Rx (1,2) = -1*sin(roll);
    Rx (2,1) = sin(roll);
    Rx (2,2) = cos(roll);

    Ry (0,0) = cos(pitch);
    Ry (0,2) = sin(pitch);
    Ry (2,0) = -1*sin(pitch);
    Ry (2,2) = cos(pitch);

    Rz (0,0) = cos(yaw);
    Rz (0,1) = -1*sin(yaw);
    Rz (1,0) = sin(yaw);
    Rz (1,1) = cos(yaw);
    std::cout<<Rx<<"\n"<<std::endl;
    std::cout<<Ry<<"\n"<<std::endl;
    std::cout<<Rz<<"\n"<<std::endl;

    Eigen::Matrix3d R = Rz * Ry *Rx;
    std::cout<<R<<"\n"<<std::endl;

    Eigen::Matrix4f camInBase;
    camInBase << 0.0118572,	-0.999928,	0.00178924,	393.625,
                 -0.989463,	-0.0114748,	0.144334,	-275.073,
                 -0.144303,	-0.00348178,	-0.989527,	1319.33,
                 0.0,	0.0,	0.0,	1.0;
    std::cout<<camInBase<<"\n"<<std::endl;

    Eigen::Affine3f H;
//    H.rotation() << 0.0118572,	-0.999928,	0.00178924,
//            -0.989463,	-0.0114748,	0.144334,
//            -0.144303,	-0.00348178,	-0.989527;
//    H.translation() << 0.393625, -0.275073, 1.31933;
    H.matrix() = camInBase;

    //
    //pcl::transformPoint(startPoint, H);
    Eigen::Vector3f startPointVector, suctionPointVector;
    startPointVector[0] = startPoint.x;
    startPointVector[1] = startPoint.y;
    startPointVector[2] = startPoint.z;

    std::cout<<"startPoint:"<<startPointVector<<"\n"<<std::endl;
    pcl::transformVector(startPointVector, suctionPointVector,H);
    std::cout<<"startPoint:"<<startPoint<<"\n"<<std::endl;
    std::cout<<"suctionPointVector:"<<suctionPointVector<<"\n"<<std::endl;

}
