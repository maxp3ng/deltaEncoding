/* mpDelta 
 * max peng 2023
 * v0.2
 */


#include <iostream>
#include <vector>
#include <string>
using namespace std;
using std::vector;

const string version = "v0.2"; 

vector<int> encode(vector<int> inputV){
	int N = inputV.size();
	vector<int> outputV(N, 0);

	outputV[0] = inputV[0];
	//0index of outputV will be the original starting point
	//
	for (int i=1; i<N; i++){
		outputV[i] = inputV[i] - inputV[i-1];
	}
	return outputV;
}

vector<int> decode(vector<int> inputV){
	int N = inputV.size();
	vector<int> outputV(N, 0);

	outputV[0] = inputV[0];
	//0index of outputV will be the original starting point
	//
	for (int i=1; i<N; i++){
		outputV[i] = outputV[i-1] + inputV[i];
	}
	return outputV;
}



void test(vector<int> &testV, string testCode, bool isEncode){

	cout<<endl;
	cout << " ------------------ test running --------------- \n";
	cout << "Test |" << testCode << "|:  \n";
	
	vector<int> codedV;

	cout << " ------------------ encoder running--------------- \n";
	if (isEncode){
		codedV = encode(testV);
	} else {
		codedV = decode(testV);
	}

	cout << " ------------------ encoder finished --------------- \n";

	int testSum = 0;
	cout << "testVector: {";
	for (int i=0; i<testV.size(); i++){
		testSum += testV[i];
		cout << testV[i] << ", ";
	}
	cout << "}  sum: " << to_string(testSum) << endl;

	int codedSum = 0;
	cout << "encodedVector: {";
	for (int i=0; i<codedV.size(); i++){
		codedSum += codedV[i];
		cout << codedV[i]  << ", ";
	}
	cout << "}  sum: " << to_string(codedSum) << endl;

	testV = codedV;
	cout << " ------------------ test finished --------------- \n";
}

	
int main(){
	cout<<endl<<endl<<endl;
	cout << "maxPeng 2023 --- mpDelta" << endl;
	cout << "Version " << version << endl;
	cout << "************************ program start **************** \n"; 

	// cout<<endl<<endl<<endl;
	// cout << "**************** 1TO10 TESTS **************** \n";
	// vector<int> oneToTenV{1,2,3,4,5,6,7,8,9,10};

	// test(oneToTenV, "1TO10 ENCODE 1", true);
	// test(oneToTenV, "1TO10 ENCODE 2", true);
	// test(oneToTenV, "1TO10 DECODE 1", false);
	// test(oneToTenV, "1TO10 DECODE 2", false);


	// cout<<endl<<endl<<endl;
	// cout << "**************** RANDOM TESTS **************** \n";
	// vector<int> randomV{1,2,7,4,32,8,2,3,5,2,3,4,8,13,2};

	// test(randomV, "RANDOM", true);
	// test(randomV, "RANDOM", true);
	// test(randomV, "RANDOM", false);
	// test(randomV, "RANDOM", false);

	// cout<<endl<<endl<<endl;
	// cout << "**************** DESCENDING **************** \n";
	// vector<int> descendV{10,9,8,7,6,5,4,3,2,1};

	// test(descendV, "DESCENDING", true);
	// test(descendV, "DESCENDING", true);
	// test(descendV, "DESCENDING", false);
	// test(descendV, "DESCENDING", false);

	cout<<endl<<endl<<endl;
	cout << "**************** POW2 **************** \n";
	vector<int> pow2V{1,4,9,16,25,36,49,64,81,100,81,64,49,36,25,16,9,4,1};

	test(pow2V, "POW2", true);
	test(pow2V, "POW2", true);
	test(pow2V, "POW2", true);
	test(pow2V, "POW2", false);
	test(pow2V, "POW2", false);
	test(pow2V, "POW2", false);



	cout<<endl<<endl<<endl;
	cout << "************************ program end **************** \n"; 
	return 0;
}