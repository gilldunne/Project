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
                    if(response.length==0)  $('.buildjobUsageGraph').append('<h2>Boom</h2>');
                    else {
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
            var w = 450;
            var h = 400;
            var labelArea = 150;
            var colours = ["#99C2EB", "#0066CC", "#337DC6"];
            var color = d3.scale.category20();
            var outerRadius = (w - labelArea) / 2;
            var innerRadius = 0;
            var arc = d3.svg.arc()
                .innerRadius(innerRadius)
                .outerRadius(outerRadius);
            var pie = d3.layout.pie();
            //Create SVG element
            var svg = d3.select(".buildjobUsageGraph")
                .append("svg")
                .attr("width", w)
                .attr("height", h);

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
                    return color(i);
                })
                .attr("d", arc);

            arcs.append("path")
                .attr("fill", function (d, i) {
                    return color(i);
                })
                .attr("d", arc)
                .on("mouseover", function (d) {
                    d3.select(this)
                        .attr("fill", "#64707D");
                })
                .on("mouseout", function (d, i) {
                    d3.select(this)
                        .attr("fill", color(i));
                });
            //Labels
            arcs.append("text")
                .attr("transform", function (d) {
                    return "translate(" + arc.centroid(d) + ")";
                })
                .attr("text-anchor", "middle")
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

            legend.append("rect")
                .attr("x", w - 18)
                .attr("width", 15)
                .attr("height", 15)
                .style("fill", function (d, i) {
                    return color(i);
                });

            legend.append("text")
                .attr("x", w - 24)
                .attr("y", 9)
                .attr("dy", ".35em")
                .style("text-anchor", "end")
                .text(function (d) {
                    return d.status;
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