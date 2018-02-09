<html>
<head>
	<title>Breakthrough with AI</title>
	<link rel="stylesheet" href="static/tether.min.css">
	<link rel="stylesheet" href="static/bootstrap.min.css">

<style>
.holder {
	margin-top: 30px;
	border: 1px #000 dashed;
}
.my-col {
	float:left;
	border: 1px solid rgba(44, 62, 80, 0.3);
	background: #EDF0CF;
}
</style>
</head>
<body>
	
	<center>
		<h2>SHOWING JUST ONE MOVE TO TEST</h2>
		<button id="start" class="btn btn-success">Start</button>

		<div class="holder">
		  <div id="table" class="table"></div>
		</div>
	<center>
	

<script src="static/jquery.min.js"></script>
<script src="static/tether.min.js"></script>
<script src="static/bootstrap.min.js"></script>
<script src="static/jquery.color.min.js"></script>
<script>

	var my_table = {{ !table }};

	var row = my_table.length;
	var col = my_table[0].length;

		// This might need some changes after template
	var ratio = col/row;
	var scale = 0.4;
	var holder_width = $(document).width();
	var holder_height = $(document).height();

	if(col >= row){
		$(".holder").css("width", holder_width * scale);
		$(".holder").css("height", holder_width * scale / ratio);
	}
	else {
		$(".holder").css("width", holder_height * scale * ratio);
		$(".holder").css("height", holder_height * scale);
	}

	for (i = 0; i < row; i++)
	{
		$("#table").append('<div id="row-'+i+'"></div>');

		$("#row-"+i).addClass("my-row");

		for (j = 0; j < col; j++)
		{
			$("#row-"+i).append("<div id='col-"+i+"-"+j+"'></div>");

			$("#col-"+i+"-"+j).addClass("my-col");

			beautify(i, j);
		}
	}

	$(".my-col").css("width", $(".holder").width()/col);
	$(".my-col").css("height", $(".holder").height()/row);
						

	// helper functions
	function run()
	{
		/*
			TO SHOW THE WHOLE GAME I NEED FORMAT [[pos1, next_position1],[pos2, next_position2] ... ]

			Running for loop on list of lists
		*/
		var start_color = $("#col-4-2").css("background-color");
		var end_color = $("#col-3-3").css("background-color");

		$("#col-4-2").animate({ backgroundColor: "#45aaf2"}, 500, function(){
			$("#col-3-3").css("background", "#2ecc71");
			$("#col-3-3").animate({opacity: 1}, 800, function(){
				// Make a move
				$("#col-4-2").children().appendTo($("#col-3-3"));
				// reset background colors
				$("#col-4-2").css("background", start_color);
				$("#col-3-3").css("background", end_color);
			});
   		});
	}


	function beautify(i, j)
	{
		if (i % 2 == 0 && j % 2 == 1)
		{
			$("#col-"+i+"-"+j).css("background", "#6C9B4F");
		}
		if (i % 2 == 1 && j % 2 == 0)
		{
			$("#col-"+i+"-"+j).css("background", "#6C9B4F");
		}
		
		var pawn_height = $(".holder").height()/row;
		var black = "<img src='static/img/black_pawn.png' class='pawn' height='"+pawn_height+"'>";
		var white = "<img src='static/img/white_pawn.png' class='pawn' height='"+pawn_height+"'>";

		if (my_table[i][j] == "X")
		{
			$("#col-"+i+"-"+j).append(black);
		}
		else if (my_table[i][j] == "O")
		{
			$("#col-"+i+"-"+j).append(white);
		}
	}

	$("#start").click(run);



</script>
</body>
</html>