import React from 'react'
import axios from 'axios'

import Auth from '../../lib/Auth'

import BarForm from './BarForm'

class BarsNew extends React.Component {
  constructor() {
    super()

    this.state = {
      data: {
        name: '',
        address: '',
        lat: '',
        lng: '',
        terrace: '',
        description: '',
        hero: '',
        location: ''
      },
      errors: {}
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.suggestionSelect = this.suggestionSelect.bind(this)
  }

  handleChange({ target: { name, value }}) {
    console.log(this.state.data)
    const data = {...this.state.data, [name]: value}
    this.setState({ data })
  }

  handleSubmit(e) {
    e.preventDefault()
    console.log(this.state.data)
    axios
      .post('/api/bars', this.state.data,
        { headers: {Authorization: `Bearer ${Auth.getToken()}`}})
      .then(this.props.history.push('/crawls/new'))
      .catch(err => console.log(err.response))
  }

  suggestionSelect(result, lat, lng) {
    // console.log(address)
    const data = {...this.state.data, address: result, lat: lat, lng: lng }
    const errors = {...this.state.errors, address: '' }
    this.setState({ data, errors })
  }

  render() {
    return(
      <main className="section grey-background">
        <div className="container">
          <BarForm
            errors={this.state.errors}
            data={this.state.data}
            handleChange={this.handleChange}
            handleSubmit={this.handleSubmit}
            suggestionSelect={this.suggestionSelect}
          />
        </div>
      </main>
    )
  }
}

export default BarsNew
