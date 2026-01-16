function predict() {
    const data = {
        mean_radius: document.getElementById("mean_radius").value,
        mean_perimeter: document.getElementById("mean_perimeter").value,
        mean_area: document.getElementById("mean_area").value,
        mean_concave_points: document.getElementById("mean_concave_points").value,
        mean_concavity: document.getElementById("mean_concavity").value,
        worst_radius: document.getElementById("worst_radius").value,
        worst_perimeter: document.getElementById("worst_perimeter").value,
        worst_area: document.getElementById("worst_area").value,
        worst_concave_points: document.getElementById("worst_concave_points").value,
        worst_concavity: document.getElementById("worst_concavity").value
    };

    fetch("/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText = data.result;
    });
}
