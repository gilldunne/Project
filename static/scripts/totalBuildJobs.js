var totalBuildjobsObj = function(){
    var init = function() {
        $('.totalBuildJobs').empty();
        var data = [];
        var names = [];

        var getRequest = function (params, callbackResponse) {
        //var getRequest = function (callbackResponse) {
            $.ajax({
                type: "GET",
                url: "/api/get_build_job_collection",
                data: params,
                cache: false,

                success: function (response) {
                    if(response.length==0)
                        $('.totalBuildJobs').append('<h2>No Graph to for this data</h2>');
                    else {
                        $('.totalBuildJobs').append(
                            '<div class="lotusui30">'+
                                '<div class="lotusHeading">'+
                                    '<h1 class="title">Total Number Servers</h1>' +
                                '</div>'+
                                '<p>The graph below displays the total number of servers per Team. This data is based on there being ' +
                                '<br>one unique Buildjob name per Server. </p><br>' +
                            '</div>');
                            callbackResponse(response);
                    }
                }
            });
        };

        var callbackResponse = function (response) {
            $.each(response, function (i, val) {
                data[i] = val.buildjob;
                names[i] = val.name;
            });

            var tip = d3.tip()
                .attr('class', 'd3-tip')
                .offset([-10, 0])
                .html(function (d) {
                    return "<strong>Total:</strong> <span style='color:black'>" + d + "</span>";
                });

            var margin = {top: 30, right: 20, bottom: 20, left: 155},
                width = 520,
                barHeight = 30,
                height = barHeight * data.length;

            var x = d3.scale.linear()
                .domain([0, d3.max(data)])
                .range([0, width]);

            var y = d3.scale.ordinal()
                .domain(names)
                .rangeBands([0, height]);

            var y1 = d3.scale.ordinal()
                .domain(data)
                .rangeBands([0, height]);

            var xAxis = d3.svg.axis()
                .scale(x)
                .orient("top")
                .tickSize(-height);

            var chart = d3.select(".totalBuildJobs")
                .append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

            chart.call(tip);

            chart.append("g")
                .attr("fill", "#4775FF")
                .attr("class", "bars")
                .selectAll("rect")
                .data(data)
                .enter().append("rect")
                .attr("y", function (d, i) {
                    return i * barHeight;
                })
                .attr("height", barHeight - 1)
                .attr("width", x);

            chart.append("g")
                .attr("class", "axis")
                .call(xAxis)
                .select(".tick line")
                .style("stroke", "#000");

            chart.selectAll("text.name")
                .data(names)
                .enter().append("text")
                .attr("x", -155)
                .attr("y", function (d) {
                    return y(d) + barHeight / 2;
                })
                .attr("dy", ".36em")
                .attr("text-anchor", "right")
                .attr('class', 'name')
                .text(String);

            chart.selectAll("rect")
                .on('mouseover', tip.show)
                .on('mouseout', tip.hide)
                .on('click', function (d, i) {
                    sessionStorage.setItem("teamName", names[i]);
                    console.log(names[i]);
                    var a = componentBuildJobsObj.init();
                    var b = activeInuseServersObj.init();

                    $(".buildjobUsageGraph").hide();
                    $(".totalBuildJobs").hide();
                    $(".chart").show();
                    $(".activeInuseServerGraph").show();
                })
            ;
        };

        var params = "computerName="+sessionStorage.getItem("computerName");
        getRequest(params, callbackResponse);
        //getRequest(callbackResponse);
    };
    init();
    return{
        init:init
    };
}();