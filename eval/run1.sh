ori_name=news_transfer1
tar_test=test1

mkdir ${tar_test}
mkdir ${tar_test}/embedding
mkdir ${tar_test}/embedding1
mkdir ${tar_test}/embedding2
mkdir ${tar_test}/embedding3
mkdir ${tar_test}/embedding4
mkdir ${tar_test}/embedding5
mkdir ${tar_test}/embedding6
mkdir ${tar_test}/embedding7
mkdir ${tar_test}/embedding8


cp ../model/data/q_test.txt ${tar_test}/
cp ../model/data/s_test.txt ${tar_test}/

cp ../model/${ori_name}/session_style/q_test_style0.txt ${tar_test}/embedding/style0.txt
cp ../model/${ori_name}/session_style/q_test_style1.txt ${tar_test}/embedding/style1.txt

cp ../model/${ori_name}/session_style1/q_test_style0.txt ${tar_test}/embedding1/style0.txt
cp ../model/${ori_name}/session_style1/q_test_style1.txt ${tar_test}/embedding1/style1.txt

cp ../model/${ori_name}/session_style2/q_test_style0.txt ${tar_test}/embedding2/style0.txt
cp ../model/${ori_name}/session_style2/q_test_style1.txt ${tar_test}/embedding2/style1.txt

cp ../model/${ori_name}/session_style3/q_test_style0.txt ${tar_test}/embedding3/style0.txt
cp ../model/${ori_name}/session_style3/q_test_style1.txt ${tar_test}/embedding3/style1.txt

cp ../model/${ori_name}/session_style4/q_test_style0.txt ${tar_test}/embedding4/style0.txt
cp ../model/${ori_name}/session_style4/q_test_style1.txt ${tar_test}/embedding4/style1.txt

cp ../model/${ori_name}/session_style5/q_test_style0.txt ${tar_test}/embedding5/style0.txt
cp ../model/${ori_name}/session_style5/q_test_style1.txt ${tar_test}/embedding5/style1.txt

cp ../model/${ori_name}/session_style6/q_test_style0.txt ${tar_test}/embedding6/style0.txt
cp ../model/${ori_name}/session_style6/q_test_style1.txt ${tar_test}/embedding6/style1.txt

cp ../model/${ori_name}/session_style7/q_test_style0.txt ${tar_test}/embedding7/style0.txt
cp ../model/${ori_name}/session_style7/q_test_style1.txt ${tar_test}/embedding7/style1.txt

cp ../model/${ori_name}/session_style8/q_test_style0.txt ${tar_test}/embedding8/style0.txt
cp ../model/${ori_name}/session_style8/q_test_style1.txt ${tar_test}/embedding8/style1.txt
