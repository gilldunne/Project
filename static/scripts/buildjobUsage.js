var buildJobUsageObj = function(){
    var init = function() {

        $('.buildjobUsageGraph').empty();
        var datasetCount = [];

        var getRequest = function (params, callbackResponseUsage) {
            $.ajax({
                type: "GET",
                data: params,
                url: "/api/get_build_job_usage_sub_teams",
                cache: false,
                success: function (response) {
                    if(response.length==0)
                        $('.buildjobUsageGraph').append('<h2>No Graph to for this data</h2>');
                    else {
                        $('.buildjobUsageGraph').append(
                            '<div class="lotusui30">'+
                                '<div class="lotusHeading">'+
                                    '<h1 class="title">'+ params.replace('componentName=', '')+'</h1>' +
                                '</div>'+
                                '<h3>Server Usages</h3>'+
                                '<p>The number of servers based on the usages of each component. </p><br>');
                        callbackResponseUsage(response);
                    }
                }
            });
        };
        var callbackResponseUsage = function (response) {
            pieUsage(
                $.each(response, function (i, val) {
                    datasetCount[i] = val.count;
                }));
        };

        function pieUsage(dataset) {
            var w = 500;
            var h = 330;
            var labelArea = 150;
            var color = ["#3366FF", "#2447B2", "#85A3FF"];
            var colors = d3.scale.category20();
            var outerRadius = (w - labelArea) / 2;
            var innerRadius = 90;
            var arc = d3.svg.arc()
                .innerRadius(innerRadius)
                .outerRadius(outerRadius);
            var pie = d3.layout.pie();
            //Create SVG element
            var svg = d3.select(".buildjobUsageGraph")
                .append("svg")
                .attr("width", w+20)
                .attr("height", h+20);
            var message = [];
            var tip = d3.tip()
                .attr('class', 'd3-tip')
                .offset([50, 10])
                .html(function (d, i) {
                        return "<span style='color:black'>" + message[i] + "</span>";
                });

            //Set up groups
            var arcs = svg.selectAll("g.arc")
                .data(pie(datasetCount))
                .enter()
                .append("g")
                .attr("class", "arc")
                .attr("transform", "translate(" + outerRadius + "," + outerRadius + ")");

            //Draw arc paths
            arcs.append("path")
                .attr("fill", function (d, i) {
                    return color[i];
                })
                .attr("d", arc);

            arcs.append("path")
                .attr("fill", function (d, i) {
                    return color[i];
                })
                .attr("d", arc)
                .on("mouseover", tip.show)
                .on("mouseout", tip.hide);

            arcs.call(tip);

            //Labels
            arcs.append("text")
                .attr("transform", function (d) {
                    return "translate(" + arc.centroid(d) + ")";
                })
                .attr("text-anchor", "middle")
                .style("font-size", "20px")
                .text(function (d) {
                    return d.value;
                });

            var legend = svg.selectAll(".legend")
                .data(dataset)
                .enter()
                .append("g")
                .attr("class", "legend")
                .attr("transform", function (d, i) {
                    return "translate(0," + i * 20 + ")";
                });


            legend.append("text")
                .attr("x", w - 24)
                .attr("y", 9)
                .attr("dy", ".35em")
                .style("text-anchor", "end")
                .text(function (d, i) {
                    message[i] = d.status;
                    return d.status;
                });

            legend.append("rect")
                .attr("x", w - 18)
                .attr("width", 15)
                .attr("height", 15)
                .style("fill", function (d, i) {
                    return color[i];
                });


        }

        var params = "componentName="+sessionStorage.getItem("componentName");
        getRequest(params, callbackResponseUsage);
    };
    init();
    return{
        init:init
    };
}();

