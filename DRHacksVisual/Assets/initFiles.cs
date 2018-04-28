using UnityEngine;
using System.Collections;
using System;
using System.IO;

public class initFiles : MonoBehaviour
{

	int[] id = new int[1000];
	string[] title = new string[1000];
	public static string[] type = new string[1000];
	string[] author = new string[1000];
	public static string[] uri  = new string[1000];

	public static int[] filesize = new int[1000];
	public static int x = 0;

	protected FileInfo theSourceFile = null;
	protected StreamReader reader = null;
	protected string text = " "; 

	void Start () {
		theSourceFile = new FileInfo (Application.dataPath + "/tmp.txt");
		theSourceFile = new FileInfo (Application.dataPath + "/Resources/DRHacks/tmp.txt");

		reader = theSourceFile.OpenText();


	}

	public GameObject prefab;


	int c = 0;

	void Update () {
		
		try {
			if (text != null) {
			text = reader.ReadLine();
			if (text.StartsWith("!")) {
				text = text.Remove(0,1);
				id [c] = int.Parse(text);
			}

			if (text.StartsWith("@")) {
				text = text.Remove(0,1);
				title [c] = text;
			}

			if (text.StartsWith("#")) {
				text = text.Remove(0,1);
				type [c] = text;
			}
			if (text.StartsWith("^")) {
				text = text.Remove(0,1);
				author [c] = text;
			}
			if (text.StartsWith("$")) {
				text = text.Remove(0,1);
				uri [c] = text;
			}
			if (text.StartsWith("%")) {
				text = text.Remove(0,1);
				filesize [c] = int.Parse(text);
			//	print (filesize [c]);
			}
			c++;
			}
		} catch {
		//	Array.Sort(filesize);
		}

		if (text == null) {
			if (x <= c) {
				Instantiate (prefab, new Vector3 (x * 1.2F, 0, 0), Quaternion.identity);
				x++;
			}
		}

		Vector3 moveDir = Vector3.zero;
		moveDir.x = Input.GetAxis("Horizontal"); // get result of AD keys in X
	//	moveDir.z = Input.GetAxis("Vertical"); // get result of WS keys in Z
		// move this object at frame rate independent speed:
		transform.position += moveDir * 30 * Time.deltaTime;
	
	}
}