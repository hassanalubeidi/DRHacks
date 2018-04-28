using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class initFileLook : MonoBehaviour {

	public Material[] mats;
	Material m_Material; 

	int x = initFiles.x;
	void Start () {
		m_Material = GetComponent<Renderer>().material;

		int l = initFiles.filesize [x] / 10000;
		if (l != 0 && l < 1000) {
			transform.localScale = new Vector3 (l, l, 0.1F);
		} else {
			Destroy (gameObject);
		}


		//	print ("lol" + initFiles.type [initFiles.x]);
			string ty = initFiles.type [x];
			if (ty == "article") {
			print ("lol");
			m_Material = mats[0];
			}
			if (ty == "conferance") {
			print ("lol");
			m_Material = mats[1];
			}

		m_Material = mats[0];

		} 

	void OnMouseDown(){
		string url = initFiles.uri[x];
		print (url);
		Application.OpenURL(url);
	}
	// Update is called once per frame
	void Update () {
		
	}
}
