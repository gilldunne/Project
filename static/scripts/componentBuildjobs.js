var componentBuildJobsObj = function() {
    var init = function(){
        $('.chart').empty();
        var  data = [];
        var names = [];

        var getRequest = function (params, callbackResponse) {
            $.ajax({
                type: "GET",
                data: params,
                url: "/api/get_build_job_collection_component_names",
                cache: false,

                success: function (response) {
                    if(response.length==0)
                        $('.chart').append('<h2>No Graph to for this data</h2>');
                    else {
                        $('.chart').append(
                            '<div class="lotusui30">'+
                                '<div class="lotusHeading">'+
                                    '<h1>'+ params.replace(/teamName=|&computerName=|test1.uk.ibm.com|test1.ie.ibm.com|null/g, '')+'<h1>'+
                                '</div>'+
                                '<h3>Number of Servers for each Component</h3>' +
                                '<p>The below graph shows the number of servers for each component on the team</p><br>'+
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
                width = 530,
                barHeight = 25,
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

            var chart = d3.select(".chart")
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
                .attr("x", -150)
                .attr("y", function (d) {
                    return y(d) + barHeight / 2;
                })
                .attr("dy", ".36em")
                .attr("text-anchor", "right")
                .attr('class', 'name')
                .text(String);

            chart.selectAll("rect")
                .on('mouseover', tip.show)
                .on('mouseout', tip.hide);

        };

        var params= "teamName="+sessionStorage.getItem("teamName")+"&"+"computerName="+sessionStorage.getItem("computerName");
        getRequest(params, callbackResponse);
    };
    init();
    return{
        init:init
    }
}();

