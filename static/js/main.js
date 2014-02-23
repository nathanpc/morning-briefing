// main.js

$(document).ready(function () {
	//
});

/*$(window).resize(function () {
	if ($(window).width() < 768) {
		// Fixes the floating bug in small devices.
		dirlist.populate_grid(dirlist.current.contents);
	} else {
		// Fixes the paddings for grid on multiple resolutions.
		fix_grid_padding();
	}
});*/

/**
 *  Load a folder.
 *
 *  @param path Path to the folder.
 *  @param root Root name.
 */
dirlist.load_folder = function (path, root) {
	if (root === undefined) {
		root = dirlist.current.root;
	}

	var req = new XMLHttpRequest();
	console.log("Loading path: " + path + " (" + root + ")");

	// Completed
	req.addEventListener("load", function (event) {
		var response = JSON.parse(req.responseText);
		console.log(response);

		// Set the path and populate the grid.
		dirlist.set_path(path, response);
		dirlist.populate_grid(response);
	}, false);

	// Error
	req.addEventListener("error", function (event) {
		console.log("ERROR!");
		console.log(event);
		console.log(req);

		alert("Error! Couldn't load path: " + path + " (" + root + ")");
	}, false);

	// Setup the request.
	req.open("GET", "/list?path=" + encodeURIComponent(path) + "&root=" + encodeURIComponent(root), true);
	req.send();
}