#include <jsoncpp/json/json.h>
#include <iostream>
#include <fstream>

int main()
{
    Json::Reader reader;
    Json::Value root;

    std::string json_file_path = "../scene_score.json";
    std::ifstream file;
    file.open(json_file_path, std::ios::in);

    if(reader.parse(file, root))
    {
        std::cout << root.size() << "\n" << std::endl;
        // std::cout << root[0] << "\n" << std::endl;

        for(size_t i=0; i < root.size(); i++)
        {
            std::string scene_name = std::to_string(i);
            Json::Value scene_data = root[scene_name];
            Json::Value grasp_name = scene_data["grasp_name"];
            Json::Value grasp_score = scene_data["grasp_score"];
            Json::Value mask_centroid_x_list = scene_data["mask_centroid_x"];

            // std::cout << grasp_name.size() << "\n" << std::endl;
//            std::cout << grasp_name[0] << "\n" << std::endl;
//            std::string grasp_name_string = grasp_name.toStyledString();
            // std::cout << grasp_name_string << "\n" << std::endl;

            std::vector<std::string> grasp_mask_names;
            std::vector<float> grasp_scores;
            std::vector<int> mask_centroid_x;
            for(uint j=0; j<grasp_name.size(); j++)
            {
                std::string mask_name = grasp_name[j].asString();
                float score = grasp_score[j].asFloat();
                int centroid_x = mask_centroid_x_list[j].asInt();
                // std::cout << centroid_x << "\n" << std::endl;
                grasp_mask_names.push_back(mask_name);
                grasp_scores.push_back(score);
                mask_centroid_x.push_back(centroid_x);
            }




            // char const* grasp_name =  scene_data.get("grasp_name", "UTF-8").asCString();
            // std::string grasp_name = scene_data.get("grasp_name", "UTF-8").asString();
            // std::cout << grasp_name << "\n" << std::endl;

        }
    }

    return 0;
}
