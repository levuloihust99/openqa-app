import React from 'react';
import "./assets/css/base.css"
import NavBar from './components/navbar';

const App = (props) => {
	const [answers, setAnswers] = React.useState([])
	const [question, setQuestion] = React.useState('')

	const handleChange = (event) => {
		setQuestion(event.target.value)
	}

	const handleSubmit = async (event) => {
		event.preventDefault()
		const payload = JSON.stringify({
			question: question
		})
		console.log(payload)
		console.log(typeof payload)

		const requestOptions = {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: payload
        }

		const url = "http://localhost:5000/get_answers"
		const response = await fetch(url, requestOptions)
        const data = await response.json()

		setAnswers(data)
	}

	return (
		<>
			<NavBar />
			<div className="container" style={{paddingTop: "15px"}}>
				<div className="questionBar" style={{paddingBottom: "20px"}}>
					<form autoComplete="off" onSubmit={handleSubmit}>
						<label style={{display: "block", fontSize: "17px", fontWeight: "bold", marginBottom: "10px"}}>Question</label>
						<input className="inputQuestion" type="text" id="question" name="question" placeholder="Enter your question here" onChange={handleChange} />
						<button style={{paddingTop: "8px", paddingBottom: "8px", paddingLeft: "16px", paddingRight: "16px", fontSize: "14px"}} type="submit">Go</button>
					</form>
				</div>
				{
					answers.map((item) => {
						return (
							<div>
								<h3>{item.title}</h3>
								<p>{item.text}</p>
							</div>
						)
					})
				}
			</div>
		</>
	)
}

export default App;
