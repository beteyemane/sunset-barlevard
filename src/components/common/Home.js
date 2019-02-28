import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'


class Home extends React.Component{
  constructor(){
    super()

    this.state={
      crawls: []
    }

  }

  componentDidMount() {
    axios.get('/api/crawls')
      .then(res => this.setState({ crawls: res.data }))
  }

  render(){
    console.log(this.state.crawls)
    return(
      <main>
        <section className="hero is-black is-large">
          <div className="hero-body">
            <div className="container">
              <h1 className="title level-item">
                Sunset Barlevard
              </h1>
              <h2 className="subtitle">
              </h2>
            </div>
          </div>
        </section>
        <div className="crawls">
          <h1 className="title is-2 header-crawl" >Bar Crawls</h1>
          <div className="center">
            <div className="columns slider">
              {this.state.crawls.map(crawl => <div className="column is-centered is-full center" key={crawl._id}>
                <Link to={`{/crawls/${crawl._id}`}>
                  <div className="header-crawl">
                    <h1 className="title is-4">{crawl.name}</h1>
                  </div>
                  <h2 className="title is-5 header-crawl">{crawl.description}</h2>
                  <div style={{backgroundImage: `url(${crawl.stops[0].bar.hero})`}}className="carousel"/>
                </Link>
              </div>)}
            </div>
          </div>

        </div>
      </main>

    )
  }
}

export default Home