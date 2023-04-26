const url = "https://flight-radar1.p.rapidapi.com/airports/list";
const options = {
  method: "GET",
  headers: {
    "content-type": "application/octet-stream",
    "X-RapidAPI-Key": "485377d487msh108c692813b6e2ap1203a3jsn23084661da34",
    "X-RapidAPI-Host": "flight-radar1.p.rapidapi.com",
  },
};

try {
  const response = await fetch(url, options);
  const result = await response.text();
  console.log(result);
} catch (error) {
  console.error(error);
}
